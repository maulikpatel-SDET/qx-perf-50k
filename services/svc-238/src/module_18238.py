"""Service module 18238: business logic, no crypto."""


def calculate_total_18238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18238():
    return 'module 18238 handles orders and invoices'
