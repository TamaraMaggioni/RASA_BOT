from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import datetime


class ActionCheckHorario(Action):
    def name(self) -> Text:
        return "action_check_horario"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try: 
            # Obtener el día y la hora actual
            now = datetime.datetime.now()

            # Verificar si es un día laborable y dentro del horario de atención
            if now.weekday() < 5 and 8 <= now.hour < 21:
            # Si es dentro del horario, puedes continuar con el flujo de agendamiento
                dispatcher.utter_message(text="¡Hola! ¿Cómo estás? Mi nombre es Elena, la asistente virutal del Hospital. Te voy a estar ayudando a gestionar tu turno médico.") 
                return [SlotSet("horario_valido", True)] # Indicar que el horario es válido
            else:
            # Si es fuera del horario, enviar el mensaje correspondiente
                dispatcher.utter_message(text="Gracias por comunicarte con nuestro canal virtual de turnos. Nuestro horario de atención es de lunes a viernes de 8 a 17 hs, por lo que te solicitamos nos vuelvas a escribir en ese rango horario. ¡Muchas gracias!")
                return [SlotSet("horario_valido", False)]  # Indicar que el horario NO es válido   
        
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir
            dispatcher.utter_message(text="Lo siento, ocurrió un error al procesar tu solicitud. Por favor, intantalo de nuevo más tarde.")
            # Opcionalmente, puedes registrar el error para depurarlo más tarde
            print(f"Error en action_check_horario: {e}")
            return []  # No establecer ningún slot en caso de error


class ActionResetForm(Action):
    def name(self):
        return "action_reset_form"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("nombre_apellido", None),
            SlotSet("dni", None),
            SlotSet("obra_social", None),
            SlotSet("paciente_nuevo", None),
        ]
        
class ActionResetForm2(Action):
    def name(self):
        return "action_reset_form_2"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("especialidad", None)
        ]  

class ActionRetomarMotivoInicial(Action):
    def name(self) -> str:
        return "action_retomar_motivo_inicial"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        # Obtener el valor del slot 'motivo_turno'
        motivo_turno = tracker.get_slot('motivo_turno')

        # Responder según el motivo inicial de la llamada
        if motivo_turno == "solicitar_turno":
            dispatcher.utter_message(text="Perfecto, continuemos con la solicitud del turno.")
            dispatcher.utter_message(response="utter_tipo_de_turno")  # Respuesta para solicitar turno

        elif motivo_turno == "modificar_turno":
            dispatcher.utter_message(text="Perfecto, continuemos con la modificación del turno.")
            dispatcher.utter_message(response="utter_modificar_turno")  # Respuesta para modificar turno

        elif motivo_turno == "cancelar_turno":
            dispatcher.utter_message(text="Perfecto, continuemos con la cancelación del turno.")
            dispatcher.utter_message(response="utter_cancelar_turno")  # Respuesta para cancelar turno

        # Devolver una lista vacía de eventos ya que no se están modificando los slots en esta acción
        return []


class ActionResetForm3(Action):
    def name(self) -> str:
        return "action_reset_form3"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        # Reinicia los slots relacionados con la modificación del turno y especialidad
        return [
            SlotSet("especialidad", None),
            SlotSet("fecha_hora_modificar", None)
        ]