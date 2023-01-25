import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def hanoi_tower_loop(n):
    # Предположим, что диски на первой башне
    tower_01 = list(range(1, n + 1))
    tower_02 = []
    tower_03 = []

    # Мы перемещаем диски, пока первая или вторая башни не пустые
    previous_step_target = 0
    while len(tower_01) or len(tower_02):
        if tower_01 and previous_step_target != 1:
            if not tower_02 or tower_02[0] > tower_01[0]:
                logger.info(f"Перемещаем диск {chr(64 + tower_01[0])} 1 -> 2")
                previous_step_target = 2

                tower_02.insert(0, tower_01[0])
                del tower_01[0]
                continue

            if not tower_03 or tower_03[0] > tower_01[0]:
                logger.info(f"Перемещаем диск {chr(64 + tower_01[0])} 3 -> 1")
                previous_step_target = 3

                tower_03.insert(0, tower_01[0])
                del tower_01[0]
                continue

        if tower_02 and previous_step_target != 2:
            if not tower_03 or tower_03[0] > tower_02[0]:
                logger.info(f"Перемещаем диск {chr(64 + tower_02[0])} 2 -> 3")
                previous_step_target = 3

                tower_03.insert(0, tower_02[0])
                del tower_02[0]
                continue

            if not tower_01 or tower_01[0] > tower_02[0]:
                logger.info(f"Перемещаем диск {chr(64 + tower_02[0])} 2 -> 1")
                previous_step_target = 1

                tower_01.insert(0, tower_02[0])
                del tower_02[0]
                continue

        if tower_03 and previous_step_target != 3:
            if not tower_02 or tower_02[0] > tower_03[0]:
                logger.info(f"Перемещаем диск {chr(64 + tower_03[0])} 3 -> 2")
                previous_step_target = 2

                tower_02.insert(0, tower_03[0])
                del tower_03[0]
                continue

            if not tower_01 or tower_01[0] > tower_03[0]:
                logger.info(f"Перемещаем диск {chr(64 + tower_03[0])} 3 -> 1")
                previous_step_target = 1

                tower_01.insert(0, tower_03[0])
                del tower_03[0]
                continue


def hanoi_tower_recursive(n, source: int = 0, target: int = 2):
    if n > 0:
        buffer = 3 - source - target
        hanoi_tower_recursive(n - 1, source, buffer)
        logger.info(f"Перемещаем диск {chr(64 + n)} {source + 1} -> {target + 1}")
        hanoi_tower_recursive(n - 1, buffer, target)


def main():
    logger.info("Ханойские башни в цикле")
    hanoi_tower_loop(4)

    logger.info("\n ------------------------- \n")

    logger.info("Ханойские башни рекурсивно")
    hanoi_tower_recursive(4)


if __name__ == "__main__":
    main()