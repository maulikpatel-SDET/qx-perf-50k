"""Service module 45578: business logic, no crypto."""


def calculate_total_45578(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45578():
    return 'module 45578 handles orders and invoices'
