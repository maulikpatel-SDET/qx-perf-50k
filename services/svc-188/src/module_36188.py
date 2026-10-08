"""Service module 36188: business logic, no crypto."""


def calculate_total_36188(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36188():
    return 'module 36188 handles orders and invoices'
