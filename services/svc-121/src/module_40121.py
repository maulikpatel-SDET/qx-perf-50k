"""Service module 40121: business logic, no crypto."""


def calculate_total_40121(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40121():
    return 'module 40121 handles orders and invoices'
