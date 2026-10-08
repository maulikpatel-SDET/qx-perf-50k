"""Service module 19489: business logic, no crypto."""


def calculate_total_19489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19489():
    return 'module 19489 handles orders and invoices'
