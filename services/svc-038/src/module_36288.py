"""Service module 36288: business logic, no crypto."""


def calculate_total_36288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36288():
    return 'module 36288 handles orders and invoices'
