"""Service module 25702: business logic, no crypto."""


def calculate_total_25702(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25702():
    return 'module 25702 handles orders and invoices'
