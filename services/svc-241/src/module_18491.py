"""Service module 18491: business logic, no crypto."""


def calculate_total_18491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18491():
    return 'module 18491 handles orders and invoices'
