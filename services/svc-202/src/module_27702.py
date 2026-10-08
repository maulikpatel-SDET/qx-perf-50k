"""Service module 27702: business logic, no crypto."""


def calculate_total_27702(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27702():
    return 'module 27702 handles orders and invoices'
