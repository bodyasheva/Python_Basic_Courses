from datetime import datetime, timedelta


def get_date_list(from_date: str, to_date: str) -> list[str]:
    data_standart = "%Y-%m-%d"
    start_date = datetime.strptime(from_date, data_standart)
    end_date = datetime.strptime(to_date, data_standart)
    if start_date <= end_date:
        delta = timedelta(days=1)
        res_list = []
        while start_date <= end_date:
            res_list.append(start_date.strftime(data_standart))
            start_date += delta
        return print(res_list)
    else:
        delta = timedelta(days=-1)
        res_list = []
        while start_date >= end_date:
            res_list.append(start_date.strftime(data_standart))
            start_date += delta
        return print(res_list)


get_date_list("2023-06-04", "2023-06-06")
get_date_list("2023-06-06", "2023-06-06")
get_date_list("2023-06-08", "2023-06-06")
