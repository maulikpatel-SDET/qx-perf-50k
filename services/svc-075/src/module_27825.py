"""Service module 27825: business logic, no crypto."""


def calculate_total_27825(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27825():
    return 'module 27825 handles orders and invoices'
