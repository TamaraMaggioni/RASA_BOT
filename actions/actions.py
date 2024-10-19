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




#class ActionVerificarDNI(Action):
#    def name(self) -> Text:
#        return "action_verificar_dni"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#        dni = tracker.get_slot('dni')
#        if not dni:
#            dispatcher.utter_message(text="No estás registrado en nuestro sistema.")
#            return []

#        url = f"http://127.0.0.1/clients/{dni}"
#        response = requests.get(url)

#        if response.status_code == 200:
#            data = response.json()
#            nombre = data.get("nombre", None)
#            apellido = data.get("apellido", None)
#            if nombre and apellido:
#                # Guardar los datos en los slots
#                return [SlotSet("nombre", nombre), SlotSet("apellido", apellido), SlotSet("datos_encontrados", True)]
#            else:
#                dispatcher.utter_message(text="Lo lamento, no encontramos tus datos en nuestro sistema.")
#                return [SlotSet("datos_encontrados", False)]
#        else:
#            dispatcher.utter_message(text="Hubo un error al verificar el DNI. Por favor, intenta nuevamente más tarde.")
#            return []

class ActionVerificarDNI(Action):
    def name(self) -> Text:
        return "action_verificar_dni"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dni = tracker.get_slot('dni')
        
        try:
            # Cargar el archivo Excel
            df = pd.read_excel('/home/dipsi/DataScience/FreeTECH/RASA/RASA_BOT/pacientes.xlsx')

            # Filtrar los datos del paciente por DNI
            patient_data = df[df['DNI'].astype(str) == str(dni)]

            if not patient_data.empty:
                nombre = patient_data['Nombre'].values[0]
                apellido = patient_data['Apellido'].values[0]
                obra_social = patient_data['Obra Social'].values[0]
                dispatcher.utter_message(text=f"¡Hola {nombre} {apellido}!")
                dispatcher.utter_message(template="utter_elegir_obra_social")
                
                # Guardar los datos en los slots
                return [
                    SlotSet("nombre", nombre),
                    SlotSet("apellido", apellido),
                    SlotSet("obra_social", obra_social),
                    SlotSet("datos_encontrados", True)
                ]
            else:
                dispatcher.utter_message(text="No encontramos tu DNI en nuestro sistema. Vamos a necesitar algunos datos del paciente.")
                dispatcher.utter_message(template="utter_elegir_obra_social")
                return [SlotSet("datos_encontrados", False)]
        
        except Exception as e:
            dispatcher.utter_message(text="Hubo un error al procesar tu solicitud. Por favor, inténtalo más tarde.")
            print(f"Error al ejecutar la acción: {e}")
            return []


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