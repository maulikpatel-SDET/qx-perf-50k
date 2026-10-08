"""Service module 26978: business logic, no crypto."""


def calculate_total_26978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26978():
    return 'module 26978 handles orders and invoices'
