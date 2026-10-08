"""Service module 20578: business logic, no crypto."""


def calculate_total_20578(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20578():
    return 'module 20578 handles orders and invoices'
