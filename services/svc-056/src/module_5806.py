"""Service module 5806: business logic, no crypto."""


def calculate_total_5806(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5806():
    return 'module 5806 handles orders and invoices'
