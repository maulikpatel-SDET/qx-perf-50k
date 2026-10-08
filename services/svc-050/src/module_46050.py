"""Service module 46050: business logic, no crypto."""


def calculate_total_46050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46050():
    return 'module 46050 handles orders and invoices'
