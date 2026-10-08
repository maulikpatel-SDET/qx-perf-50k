"""Service module 11098: business logic, no crypto."""


def calculate_total_11098(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11098():
    return 'module 11098 handles orders and invoices'
