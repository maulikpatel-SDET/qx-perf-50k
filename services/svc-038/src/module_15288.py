"""Service module 15288: business logic, no crypto."""


def calculate_total_15288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15288():
    return 'module 15288 handles orders and invoices'
