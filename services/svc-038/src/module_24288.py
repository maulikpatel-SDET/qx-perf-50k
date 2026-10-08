"""Service module 24288: business logic, no crypto."""


def calculate_total_24288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24288():
    return 'module 24288 handles orders and invoices'
