"""Service module 24978: business logic, no crypto."""


def calculate_total_24978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24978():
    return 'module 24978 handles orders and invoices'
