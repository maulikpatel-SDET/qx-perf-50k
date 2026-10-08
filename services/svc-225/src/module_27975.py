"""Service module 27975: business logic, no crypto."""


def calculate_total_27975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27975():
    return 'module 27975 handles orders and invoices'
