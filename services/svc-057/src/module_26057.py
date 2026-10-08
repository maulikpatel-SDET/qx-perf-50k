"""Service module 26057: business logic, no crypto."""


def calculate_total_26057(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26057():
    return 'module 26057 handles orders and invoices'
