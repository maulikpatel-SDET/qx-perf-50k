"""Service module 45978: business logic, no crypto."""


def calculate_total_45978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45978():
    return 'module 45978 handles orders and invoices'
