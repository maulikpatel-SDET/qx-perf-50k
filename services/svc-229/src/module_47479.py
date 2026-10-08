"""Service module 47479: business logic, no crypto."""


def calculate_total_47479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47479():
    return 'module 47479 handles orders and invoices'
