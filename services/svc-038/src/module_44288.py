"""Service module 44288: business logic, no crypto."""


def calculate_total_44288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44288():
    return 'module 44288 handles orders and invoices'
