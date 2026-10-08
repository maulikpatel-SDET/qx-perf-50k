"""Service module 9986: business logic, no crypto."""


def calculate_total_9986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9986():
    return 'module 9986 handles orders and invoices'
