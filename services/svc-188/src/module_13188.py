"""Service module 13188: business logic, no crypto."""


def calculate_total_13188(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13188():
    return 'module 13188 handles orders and invoices'
