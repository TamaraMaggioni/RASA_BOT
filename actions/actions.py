from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
import datetime
import requests
import pandas as pd


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
                dispatcher.utter_message(text="¡Hola! ¿Cómo estás? Mi nombre es Elena, la asistente virutal del Hospital. Te voy a estar ayudando con la gestión de tus turnos.") 
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


class ActionVerificarDNI(Action):
    def name(self) -> Text:
        return "action_verificar_dni"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dni = tracker.get_slot("dni")

        try:
            df = pd.read_excel("/home/dipsi/DataScience/FreeTECH/RASA/RASA_BOT/pacientes.xlsx")
            patient_data = df[df["DNI"].astype(str) == str(dni)]

            if patient_data.empty:
                dispatcher.utter_message(text="No encontramos tu DNI en nuestro sistema. Vamos a necesitar algunos datos del paciente.")
                return [
                    SlotSet("nombre", None),
                    SlotSet("apellido", None),
                    SlotSet("obra_social", None),
                    SlotSet("datos_encontrados", False)
                ]
            
            else:
               #Si se encuentra el paciente:
                nombre = patient_data["Nombre"].values[0]
                apellido = patient_data["Apellido"].values[0]
                obra_social = patient_data["Obra Social"].values[0]

                dispatcher.utter_message(text=f"¡Hola {nombre} {apellido}!")

                return [
                    SlotSet("nombre", nombre),
                    SlotSet("apellido", apellido),
                    SlotSet("obra_social", obra_social),
                    SlotSet("datos_encontrados", True)
                ]

        except Exception as e:
            dispatcher.utter_message(text="Hubo un error al procesar tu solicitud. Por favor, intentá más tarde.")
            print(f"Error en action_verificar_dni: {e}")
            return []


class ActionEvaluarObraSocial(Action):
    def name(self) -> Text:
        return "action_evaluar_obra_social"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        obra_social = tracker.get_slot("obra_social")
        obras_validas = ["PAMI", "SWISS MEDICAL", "OSDE"]

        if obra_social and obra_social.upper() in [o.upper() for o in obras_validas]:
            return [SlotSet("obra_social_valida", True)]
        else:
            return [SlotSet("obra_social_valida", False)]

class ActionResetForm(Action):
    def name(self):
        return "action_reset_form"
    
    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("nombre", None),
            SlotSet("apellido", None),
            SlotSet("dni", None)
        ]
       
class ActionResetForm2(Action):
    def name(self):
        return "action_reset_form_2"

    def run(self, dispatcher, tracker, domain):
        return [
            SlotSet("especialidad", None)
        ]  


class ActionResetForm3(Action):
    def name(self) -> str:
        return "action_reset_form3"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        # Reinicia los slots relacionados con la modificación del turno y especialidad
        return [
            SlotSet("especialidad", None),
            SlotSet("fecha_hora_modificar", None)
        ]