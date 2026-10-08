"""Service module 9098: business logic, no crypto."""


def calculate_total_9098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9098():
    return 'module 9098 handles orders and invoices'
