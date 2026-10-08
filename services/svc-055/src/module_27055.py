"""Service module 27055: business logic, no crypto."""


def calculate_total_27055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27055():
    return 'module 27055 handles orders and invoices'
