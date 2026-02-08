"""Simulación de cruce vial con 3 semáforos y LEDs NeoPixel.

Cada semáforo está compuesto por 3 LEDs NeoPixel.
- Verde: solo 1 LED encendido (los otros 2 apagados).
- Amarillo: parpadea cada 500 ms durante 3 s (solo 1 LED encendido).
- Rojo: los 3 LEDs en rojo fijo.

Al inicio, los tres semáforos parpadean en rojo por 10 s (on/off cada 500 ms).
"""

import time

from neopixel import Neopixel

# Configuración general del NeoPixel (ajusta según tu hardware).
PIN_NEOPIXEL = 0
STATE_MACHINE = 0
NUM_SEMAFOROS = 3
LEDS_POR_SEMAFORO = 3
TOTAL_LEDS = NUM_SEMAFOROS * LEDS_POR_SEMAFORO

# Colores RGB
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)
APAGADO = (0, 0, 0)

# Tiempos (segundos)
TIEMPO_VERDE = 10
TIEMPO_AMARILLO = 3
TIEMPO_PARPADEO = 0.5
TIEMPO_INICIO_ROJO_PARPADEO = 10


class SemaforoController:
    """Controla 3 semáforos sobre una tira NeoPixel."""

    def __init__(self, neopixel):
        self.neopixel = neopixel

    def _base_index(self, semaforo_id):
        return semaforo_id * LEDS_POR_SEMAFORO

    def _set_semaforo_apagado(self, semaforo_id):
        base = self._base_index(semaforo_id)
        for offset in range(LEDS_POR_SEMAFORO):
            self.neopixel.set_pixel(base + offset, APAGADO)

    def set_semaforo_rojo(self, semaforo_id):
        base = self._base_index(semaforo_id)
        for offset in range(LEDS_POR_SEMAFORO):
            self.neopixel.set_pixel(base + offset, ROJO)

    def set_semaforo_verde(self, semaforo_id):
        self._set_semaforo_apagado(semaforo_id)
        base = self._base_index(semaforo_id)
        self.neopixel.set_pixel(base, VERDE)

    def set_semaforo_amarillo(self, semaforo_id):
        self._set_semaforo_apagado(semaforo_id)
        base = self._base_index(semaforo_id)
        self.neopixel.set_pixel(base, AMARILLO)

    def mostrar(self):
        self.neopixel.show()

    def inicial_rojo_parpadeo(self):
        """Parpadea los tres semáforos en rojo por 10 segundos."""
        ciclos = int(TIEMPO_INICIO_ROJO_PARPADEO / TIEMPO_PARPADEO)
        for i in range(ciclos):
            color = ROJO if i % 2 == 0 else APAGADO
            for semaforo_id in range(NUM_SEMAFOROS):
                base = self._base_index(semaforo_id)
                for offset in range(LEDS_POR_SEMAFORO):
                    self.neopixel.set_pixel(base + offset, color)
            self.mostrar()
            time.sleep(TIEMPO_PARPADEO)

    def ciclo_semaforo(self):
        """Ejecuta el ciclo continuo de los semáforos."""
        while True:
            for semaforo_activo in range(NUM_SEMAFOROS):
                for semaforo_id in range(NUM_SEMAFOROS):
                    if semaforo_id == semaforo_activo:
                        self.set_semaforo_verde(semaforo_id)
                    else:
                        self.set_semaforo_rojo(semaforo_id)
                self.mostrar()
                time.sleep(TIEMPO_VERDE)

                parpadeos = int(TIEMPO_AMARILLO / TIEMPO_PARPADEO)
                for i in range(parpadeos):
                    for semaforo_id in range(NUM_SEMAFOROS):
                        if semaforo_id == semaforo_activo:
                            if i % 2 == 0:
                                self.set_semaforo_amarillo(semaforo_id)
                            else:
                                self._set_semaforo_apagado(semaforo_id)
                        else:
                            self.set_semaforo_rojo(semaforo_id)
                    self.mostrar()
                    time.sleep(TIEMPO_PARPADEO)


def main():
    neopixel_strip = Neopixel(TOTAL_LEDS, STATE_MACHINE, PIN_NEOPIXEL, mode="RGB")
    controlador = SemaforoController(neopixel_strip)
    controlador.inicial_rojo_parpadeo()
    controlador.ciclo_semaforo()


if __name__ == "__main__":
    main()
