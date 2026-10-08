"""Service module 27313: business logic, no crypto."""


def calculate_total_27313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27313():
    return 'module 27313 handles orders and invoices'
