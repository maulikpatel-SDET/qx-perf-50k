"""Service module 27656: business logic, no crypto."""


def calculate_total_27656(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27656():
    return 'module 27656 handles orders and invoices'
