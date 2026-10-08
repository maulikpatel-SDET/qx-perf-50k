"""Service module 21935: business logic, no crypto."""


def calculate_total_21935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21935():
    return 'module 21935 handles orders and invoices'
