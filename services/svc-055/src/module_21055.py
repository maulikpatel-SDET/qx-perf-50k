"""Service module 21055: business logic, no crypto."""


def calculate_total_21055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21055():
    return 'module 21055 handles orders and invoices'
