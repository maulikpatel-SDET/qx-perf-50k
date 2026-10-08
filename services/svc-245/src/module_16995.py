"""Service module 16995: business logic, no crypto."""


def calculate_total_16995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16995():
    return 'module 16995 handles orders and invoices'
