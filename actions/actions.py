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
            if now.weekday() < 5 and 8 <= now.hour < 17:
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
            
            