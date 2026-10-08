"""Service module 1098: business logic, no crypto."""


def calculate_total_1098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1098():
    return 'module 1098 handles orders and invoices'
