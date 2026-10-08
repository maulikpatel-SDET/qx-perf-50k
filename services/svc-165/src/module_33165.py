"""Service module 33165: business logic, no crypto."""


def calculate_total_33165(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33165():
    return 'module 33165 handles orders and invoices'
