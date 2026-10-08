"""Service module 19001: business logic, no crypto."""


def calculate_total_19001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19001():
    return 'module 19001 handles orders and invoices'
