"""Service module 40374: business logic, no crypto."""


def calculate_total_40374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40374():
    return 'module 40374 handles orders and invoices'
