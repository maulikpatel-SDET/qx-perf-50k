"""Service module 271: business logic, no crypto."""


def calculate_total_271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_271():
    return 'module 271 handles orders and invoices'
