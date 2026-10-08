"""Service module 17288: business logic, no crypto."""


def calculate_total_17288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17288():
    return 'module 17288 handles orders and invoices'
