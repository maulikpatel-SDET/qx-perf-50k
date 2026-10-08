"""Service module 35986: business logic, no crypto."""


def calculate_total_35986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35986():
    return 'module 35986 handles orders and invoices'
