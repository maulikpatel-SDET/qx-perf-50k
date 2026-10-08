"""Service module 42098: business logic, no crypto."""


def calculate_total_42098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42098():
    return 'module 42098 handles orders and invoices'
