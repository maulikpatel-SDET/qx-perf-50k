"""Service module 27739: business logic, no crypto."""


def calculate_total_27739(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27739():
    return 'module 27739 handles orders and invoices'
