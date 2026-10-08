"""Service module 17857: business logic, no crypto."""


def calculate_total_17857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17857():
    return 'module 17857 handles orders and invoices'
