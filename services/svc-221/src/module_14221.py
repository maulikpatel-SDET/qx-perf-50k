"""Service module 14221: business logic, no crypto."""


def calculate_total_14221(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14221():
    return 'module 14221 handles orders and invoices'
