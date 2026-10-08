"""Service module 21288: business logic, no crypto."""


def calculate_total_21288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21288():
    return 'module 21288 handles orders and invoices'
