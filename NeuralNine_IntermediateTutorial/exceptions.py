from logger import logger

values = [10, 5, 6, 0, 9, 8, "Hello",2]

for value in values:
    try:
        print(10/int(value))
    except (ValueError, ZeroDivisionError) as e:
        logger.warning(f'{str(e)};')
        pass
    except AttributeError as e:
        logger.error(f'{str(e)}')
        print('Moving on...')
        continue
    except Exception as e:
        logger.critical(f'{str(e)}, can not do that')
        raise