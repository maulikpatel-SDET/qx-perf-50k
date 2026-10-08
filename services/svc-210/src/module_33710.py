"""Service module 33710: business logic, no crypto."""


def calculate_total_33710(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33710():
    return 'module 33710 handles orders and invoices'
