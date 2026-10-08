"""Service module 47460: business logic, no crypto."""


def calculate_total_47460(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47460():
    return 'module 47460 handles orders and invoices'
