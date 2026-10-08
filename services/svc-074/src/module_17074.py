"""Service module 17074: business logic, no crypto."""


def calculate_total_17074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17074():
    return 'module 17074 handles orders and invoices'
